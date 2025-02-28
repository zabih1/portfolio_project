from .models import Profile

def profile_context(request):
    """
    Add profile to context for all templates
    """
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    return {
        'profile': profile
    }