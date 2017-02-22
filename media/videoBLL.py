from media.models import Video


class VideoBLL(object):
    def cad(self, values, id_item):
        obj = None
        if id_item > 0:
            obj = Video.objects.get(id=id_item)
        else:
            obj = Video()
        for item in values:
            setattr(obj, item, values[item])
        Video.save(obj)
        return obj

    def get_by_id(self, id):
        obj = Video.objects.get(id=id)
        return obj

    def lst(self):
        obj = Video.objects.filter().all()
        return obj

    def delete(self, id):
        obj = Video.objects.get(id=int(id))
        Video.delete(obj)
        return None
