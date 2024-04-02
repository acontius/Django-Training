from django.db import models
import uuid
from django.urls import reverse

class Author(models.Model):
    name      = models.CharField(max_length = 100)
    lastName  = models.CharField(max_length = 100)
    birthDate = models.DateField(blank = True , null = True)
    deathDate = models.DateField(blank = True , null = True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return '%s , %s' % (self.name , self.lastName)


class Genere(models.Model):
    name = models.CharField(max_length = 100, help_text = "The Genere (e.g. Science Fiction, French Poetry etc.)")

    #means sth to django and will add history & View on site buttons
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Book(models.Model):
    title   = models.CharField(max_length = 100 , help_text = "The book's Title (e.g. CLRS)")
    author  = models.ForeignKey(Author,null = True , on_delete = models.SET_NULL)
    summary = models.TextField(max_length = 1000 ,help_text = "What the hell is this ??",blank=True,null=True)
    genere = models.ManyToManyField(Genere,help_text = "Select a genre for this book",blank=True,null=True)

        
    def diplay_genere(self):
        return ' & '.join([ genere.name for genere in self.genere.all()[:3]])

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
    
    diplay_genere.short_description = 'Genere'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    
    class Meta:
        ordering = ["due_back"]       

    #means sth to django and will add history & View on site buttons
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self) :
        return '%s , %s' % (self.book.title , self.status)