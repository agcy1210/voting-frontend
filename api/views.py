from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from voting import models


class VoterPublickeyApiView(APIView):

    serializer_class = serializers.VoterPublickeySerializer

    def post(self, request):
        """Create hello message with our name """

        serializer = serializers.VoterPublickeySerializer(data=request.data)

        if serializer.is_valid():
            public_key = serializer.data.get('public_key')
            reference_no = serializer.data.get('reference_no')
            querysets = models.Voter.objects.filter(reference_no = reference_no)
            queryset = querysets[0]
            queryset.voter_publickey= public_key
            queryset.save()

            return Response({"message": "success!"})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CandidatePublickeyApiView(APIView):
    
    serializer_class = serializers.CandidatePublickeySerializer

    def post(self, request):
        """Create hello message with our name """

        serializer = serializers.CandidatePublickeySerializer(data=request.data)


        if serializer.is_valid():
            candidate_id = serializer.data.get('candidate_id')
            candidate_name = serializer.data.get('candidate_name')
            party_name = serializer.data.get('party_name')
            candidate_publickey = serializer.data.get('candidate_publickey')
            obj = models.Candidate(candidate_id=candidate_id,candidate_name=candidate_name,party_name=party_name,candidate_publickey=candidate_publickeyß)
            obj.save()

            return Response({"message": "success!"})



        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
