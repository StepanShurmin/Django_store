from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    """Создаёт новую статью."""
    model = Blog
    fields = ('title', 'body', 'image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """
        Преобразует заголовок блога в человекопонятный URL формат.
        Сохраняет в базе данных новый объект модели.
        """
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """Обновляет статью."""
    model = Blog
    fields = ('title', 'body', 'image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """
        Преобразует заголовок блога в человекопонятный URL формат.
        Сохраняет в базе данных новый объект модели.
        """
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        """Возвращает на страницу со статьями, после редактирования."""
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    """Выводит на экран статьи."""
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        """Фильтрует статьи по признаку-is_published."""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    """Выводит на экран отдельную статью."""
    model = Blog

    def get_object(self, queryset=None):
        """Увеличивает количество просмотров при каждом открытии статьи."""
        self.object = super().get_object(queryset)
        if self.object:
            self.object.count_views += 1
            self.object.save(update_fields=['count_views'])
        return self.object


class BlogDeleteView(DeleteView):
    """Удаляет статью."""
    model = Blog
    success_url = reverse_lazy('blog:list')
