from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)         # 제목 (최대 200자)
    content = models.TextField()                      # 내용 (길이 제한 없음)
    author = models.CharField(max_length=50, default='익명')  # 추가! -> Post 모델에 author(작성자) 필드를 추가하고, 게시글 목록에 작성자 열 표시하기
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일 (자동 저장)
    updated_at = models.DateTimeField(auto_now=True)      # 수정일 (자동 갱신)

    def __str__(self):
        return self.title