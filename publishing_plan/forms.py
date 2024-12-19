from django import forms
from django.shortcuts import redirect, render
from django_summernote.widgets import SummernoteWidget

from publishing_plan.models import Comment, PublishingPlan


class PublishingPlanForm(forms.ModelForm):
    class Meta:
        model = PublishingPlan
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
            "status",
            "contractors",
            "user",
        ]
        labels = {
            "title": "제목",
            "description": "내용",
            "start_date": "시작일",
            "end_date": "종료일",
            "status": "상태",
            "contractors": "저자",
            "user": "작성자",
        }
        widgets = {
            "description": SummernoteWidget(),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "contractors": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class PublishingPlanUpdateForm(forms.ModelForm):
    class Meta:
        model = PublishingPlan
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
            "status",
            "contractors",
        ]
        labels = {
            "title": "제목",
            "description": "내용",
            "start_date": "시작일",
            "end_date": "종료일",
            "status": "상태",
            "contractors": "저자",
        }
        widgets = {
            "description": SummernoteWidget(),
            "title": forms.TextInput(
                attrs={"class": "form-control"},
            ),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "contractors": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        labels = {
            "message": "내용",
        }
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 40,
                    "class": "form-control",
                    "placeholder": "댓글 내용을 입력해주세요.",
                }
            ),
        }

    def create_comment(request, publishing_plan_id):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.username = request.user  # 작성자 설정
                comment.publishing_plan_id = publishing_plan_id  # 관련된 일정 연결
                comment.save()
                return redirect("publishing-plan-detail", pk=publishing_plan_id)
        else:
            form = CommentForm()
        return render(request, "comment_form.html", {"form": form})
