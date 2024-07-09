from django.shortcuts import render

# Create your views here.
def listBook(request):
    books=Book.objects.all()
    paginator=Paginator(books,2)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage  :
        page=paginator.page(page_number.num_pages)



    return render(request,'user_view.html',{'books':books,'page':page})




def  detailsView(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailsview.html',{'book':book})

def Search_book(request):
    query=None
    book=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) or Q(name__icontains=query))
    else:
        book=[]
    context={'books':books,'query':query}
    return render(request,'search.html',context)

