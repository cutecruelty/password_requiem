from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenerateSerializer
from .services.generate import generate_password, pool
from .services.entropy import calculate_entropy, strength_label
from rest_framework.permissions import AllowAny

class GenerateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = GenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        length = serializer.validated_data['length']

        password = generate_password(length, pool)
        bits = calculate_entropy(length, len(pool))

        return Response({
            'password': password,
            'entropy_bits': round(bits, 1),
            'strength': strength_label(bits),
        })