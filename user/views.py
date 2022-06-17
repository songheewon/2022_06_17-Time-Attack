from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class UserView(APIView):
    def post(self, request):
        return Response({"message": "회원가입 성공!!"})


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})

    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!!"})