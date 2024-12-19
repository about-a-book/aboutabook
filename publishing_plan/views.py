from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CommentForm, PublishingPlanForm, PublishingPlanUpdateForm
from .models import Comment, PublishingPlan


class PublishingPlanCreateView(CreateView):
    """
    Publishing Plan 생성 뷰
    """

    model = PublishingPlan
    form_class = PublishingPlanForm
    template_name = "publishing_plan_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("publishing-plan-detail", kwargs={"pk": self.object.pk})


class PublishingPlanListView(ListView):
    """
    전체 목록 조회
    """

    model = PublishingPlan
    template_name = "publishing_plan_list.html"
    context_object_name = "publishing_plans"

    def get_queryset(self):
        """
        검색어(q)를 사용하여 필터링된 쿼리셋 반환
        """
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(title__icontains=q) | queryset.filter(
                description__icontains=q
            )
        return queryset


class PublishingPlanDetailView(DetailView):
    """
    Handles retrieving a specific publishing plan.
    """

    model = PublishingPlan
    template_name = "publishing_plan_detail.html"
    context_object_name = "publishing_plan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()  # 댓글 가져오기
        context["comment_form"] = CommentForm()  # 댓글 작성 폼 추가
        return context


class PublishingPlanUpdateView(UpdateView):
    """
    업데이트
    """

    model = PublishingPlan
    form_class = PublishingPlanUpdateForm
    template_name = "publishing_plan_update.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # 요청자가 작성자가 아니거나 관리자가 아니라면
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 게시글을 수정할 권한이 없습니다.")

        return obj

    def get_success_url(
        self,
    ):
        return reverse_lazy("publishing-plan-detail", kwargs={"pk": self.object.pk})


class PublishingPlanDeleteView(DeleteView):
    model = PublishingPlan
    success_url = reverse_lazy("publishing-plan-list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 글을 삭제할 권한이 없습니다.")
        return obj


class CommentCreateView(CreateView):
    model = Comment
    fields = ("message",)
    pk_url_kwarg = "publishing_plan_id"

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise Http404("로그인이 필요합니다.")

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.publishing_plan = PublishingPlan.objects.get(
            pk=self.kwargs["publishing_plan_id"]
        )
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            "publishing-plan-detail", kwargs={"pk": self.kwargs["publishing_plan_id"]}
        )


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ("message",)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 댓글을 수정할 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy(
            "publishing-plan-detail", kwargs={"pk": self.kwargs["publishing_plan_id"]}
        )


class CommentDeleteView(DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("해당 댓글을 삭제할 권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy(
            "publishing-plan-list", kwargs={"pk": self.kwargs["publishing_plan_id"]}
        )
