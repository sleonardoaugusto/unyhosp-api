from unyhosp.core.api.bed.model import Bed
import string


class UTIService(object):

    def apply_service(self, instance):
        self.create_10_beds(instance)

    @staticmethod
    def create_10_beds(instance):
        letters = string.ascii_uppercase[:10]
        for letter in letters:
            b = Bed.objects.create(
                name='Bed - {}'.format(letter),
                uti=instance
            )
            b.save()
