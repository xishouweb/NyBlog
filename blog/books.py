from blog.models import Book


def get_books(page,num):
    fromnum=(page-1)*(num-1)
    tonum=page*(num)
    result=Book.objects.order_by('-pub_date').all()[fromnum:tonum]
    return result