from django import forms
from  esprit.models import  *


class CoachForm(forms.ModelForm):
    nom = forms.CharField(max_length=100, help_text = "Enter a name")
    prenom  = forms.CharField(max_length=100, help_text = "Enter a prenom ")
    email = models.EmailField( max_length=100, help_text = "Enter a email ")
    class Meta:
        model = Coach
        fields = ('nom','prenom','email',)
class ProjectForm(forms.ModelForm):
    nom_du_projet =models.CharField( help_text = "Enter nom_du_projet", max_length=30)
    duree_du_projet  = models.IntegerField( help_text = "Enter duree_du_projet", default=0)
    temps_alloue_par_le_createur = models.EmailField( max_length=100, help_text = "Enter a temps_alloue_par_le_createur ")
    besoins = models.TextField(max_length=250, help_text = "Enter a  besoins")
    description =models.TextField(max_length=250, help_text = "Enter a  description")
    est_valide = models.BooleanField(default=False , help_text = "Enter a est_valide")
    createur =  models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )
    superviseur = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='project_coach'
    )
    membres = models.ManyToManyField(
        Student,
        through='MembershipInProject',
        # added to differ with the lead relation
        related_name='les_membres',
        blank=True,
    )
    class Meta:
        model = Project
        fields = ('nom_du_projet','duree_du_projet','temps_alloue_par_le_createur','besoins'
                  ,'description','est_valide','createur','superviseur','membres',)

class MembershipInProject(forms.ModelForm):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps alloué par le membre')
    # Meta pr dire ne peu pas etre dupliqué ds notre projet
    class Meta:
        model = MembershipInProject
        fields = ('projet', 'etudiant', 'time_allocated_by_member',)


