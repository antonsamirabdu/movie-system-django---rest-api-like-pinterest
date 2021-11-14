from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def hello(request, mykey):
    data = {'message': 'fist api {}'.format(mykey)}
    if mykey == "yes":
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    print(movies)
    serialized_movies = MovieSerializer(instance=movies, many=True)
    return Response(data=serialized_movies.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    serialized_movie=MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data=serialized_movie.errors,status=status.HTTP_400_BAD_REQUEST)

    # data = {
    #     'message': 'Success',
    #     'data': {'id': serialized_movie.data.get('id')}
    # }

    return Response(data=serialized_movie.data ,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request,pk):
    movie = Movie.objects.filter(pk=pk)
    if movie.exists():
        movie=movie.first()
    else:
        return Response(data={'message':'Failed to fine movie'},status=status.HTTP_400_BAD_REQUEST)

    serelizedMovie=MovieSerializer(instance=movie)
    return Response(data=serelizedMovie.data,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def movie_delete(request, pk):
    response = {}
    try:
        movie_selected= Movie.objects.get(pk=pk)
        movie_selected.delete()
        response['data'] = {'message':'successfully Deleted'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message': 'Error while deleting -> {}'.format(str(e))}
        response['status'] = status.HTTP_400_BAD_REQUEST

    print('result =>', response)
    return Response(**response)

@api_view(['PUT','PATCH'])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)

    except Exception as e:
        return Response(data={'message':str(e)}, status=status.HTTP_408_REQUEST_TIMEOUT)

    if request.method == 'PUT':
        serialized_movie=MovieSerializer(instance=movie,data=request.data)
    elif request.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie, data=request.data,partial=True)

    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data , status=status.HTTP_200_OK)

    return Response(data=serialized_movie.errors, status=status.HTTP_408_REQUEST_TIMEOUT)




