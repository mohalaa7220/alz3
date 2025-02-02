from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import cloudinary.uploader
from .image_processing import ImageProcessor, ModelHandler
from .models import (ProcessedImage, MainTitle, SubTitle)
from django.contrib.auth.decorators import login_required


# ============ home page =============
def home_page(request):
    return render(request, 'home.html')


# ============ psychological page =============
def psychological_page(request):
    return render(request, 'psychological.html')


# ============ about page =============
def about_page(request):
    return render(request, 'about.html')


# ============ about page =============
def info_page(request):
    main_titles = MainTitle.objects.all()
    return render(request, "info.html", {"main_titles": main_titles})


# Display details of a selected main title
def main_title_detail_view(request, pk):
    main_title = get_object_or_404(MainTitle, pk=pk)
    return render(request, "info_detail.html", {"main_title": main_title})


# View to display details of a selected subtitle
def sub_title_detail_view(request, pk):
    sub_title = get_object_or_404(SubTitle, pk=pk)
    return render(request, "sub_detail.html", {"sub_title": sub_title})


# ============ processing image page =============
@login_required
def processing_image_page(request):
    return render(request, 'processing.html')


# ============ processing image upload =============
@login_required
def process_uploaded_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            image_file = request.FILES['image']

            # Upload image to Cloudinary
            uploaded_image = cloudinary.uploader.upload(image_file)
            image_url = uploaded_image.get('url')

            # Process and predict image
            processed_image = ImageProcessor.preprocess_image(image_url)
            if processed_image is None:
                return JsonResponse({"error": "Image processing failed"}, status=400)

            severity_level, confidence_score = ModelHandler.predict(
                processed_image)

            # ✅ Save to the database
            saved_image = ProcessedImage.objects.create(
                user=request.user,
                image=image_file,
                image_url=image_url,
                result=severity_level,
                confidence_score=confidence_score
            )

            return JsonResponse({
                "id": saved_image.id,
                "result": saved_image.result,
                "image_url": saved_image.image_url,
                "confidence_score": saved_image.confidence_score
            }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


# ============ all processing image for user =============
@login_required
def all_processing_page(request):
    all_processing = ProcessedImage.objects.select_related(
        'user').filter(user=request.user).order_by('-processed_at')
    return render(request, 'all_processing.html', {'all_processing': all_processing})
