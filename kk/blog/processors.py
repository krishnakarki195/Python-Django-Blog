from . models import BlogType


def blogTypes(request):
    return {
        'blogTypes': BlogType.objects.all()
    }