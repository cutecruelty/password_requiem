from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import GenerateSerializer, PolicySerializer
from .services.generate import generate_password, pool
from .services.entropy import calculate_entropy, strength_label
from .models import GenerationLog, GenerationPolicy
from security.hibp import check_pwned
from rest_framework import generics

class GenerateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        length = serializer.validated_data['length']

        password = generate_password(length, pool)
        bits = calculate_entropy(length, len(pool))
        breach_count = check_pwned(password)

        GenerationLog.objects.create(
            length=length,
            entropy_bits=bits,
            breach_count=breach_count,
        )

        return Response({
            'password': password,
            'entropy_bits': round(bits, 1),
            'strength': strength_label(bits),
            'breach_count': breach_count,
        })
        
class PolicyListCreateView(generics.ListCreateAPIView):
    queryset = GenerationPolicy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [AllowAny]