from django.contrib import admin


# Register your models here.
from android.models import User
from android.models import Games,File,allview,videomodel,gmaeimg

admin.site.register(User)
admin.site.register(Games)
admin.site.register(File)
admin.site.register(allview)
admin.site.register(videomodel)
admin.site.register(gmaeimg)

