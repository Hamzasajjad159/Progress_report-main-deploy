# your_app/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import WorkflowStage

@receiver(post_migrate)
def create_initial_entries(sender, **kwargs):
    if sender.name == 'emp_rprt':  # Change to your app's name
        # Check if data already exists to prevent duplicates
        if not WorkflowStage.objects.exists():
            # Create initial entries
            stage1 = WorkflowStage.objects.create(title='Data Entry', order=1)
            stage4 = WorkflowStage.objects.create(title='Uploading', order=4)
            stage2 = WorkflowStage.objects.create(title='Photography', order=2)
            stage3 = WorkflowStage.objects.create(title='Editing', order=3)
            stage5 = WorkflowStage.objects.create(title='Reels', order=5)
            stage6 = WorkflowStage.objects.create(title='Marketing', order=6)

            # Defining next stages
            stage1.next_stages.add(stage2)  # Data Entry goes to Photgraphy
            stage2.next_stages.add(stage3)  # Photgraphy goes to Editing
            stage3.next_stages.add(stage4, stage5, stage6)
            
