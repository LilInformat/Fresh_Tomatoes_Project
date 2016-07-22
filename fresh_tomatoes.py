import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: Roboto;
            font-size: 12px;
            color: #424242;
            width:100%;
            height:100%;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .row{
          width:100%;
          display:flex;
        }
        .col-12{
            width:100%;
        }
        .col-8{
            width:66.66%;
        }
        .col-6{
            width:50%;
        }
        .col-4{
            width:33.33%;
        }
        .arrow_direction{
            margin-top:20px;
            font-size:2em;
        }
        .arrow_direction:hover{
            background-color: #EEE;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            display: block;
        }
        .movie-content{
            padding:10px;
            width:100%;
            height:100%;
        }
        .movie-content:hover {
            background-color: #EEE;
        }
        .movie-description{
            margin-left:20px;
            text-align:left;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .slide{
            display:none;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        @media screen and (min-width:900px){
            .body{
                width:900px;
                margin-left: auto;
                margin-right: auto;
            }
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        // Slideshow code from http://www.w3schools.com/w3css/w3css_slideshow.asp
        // Keeps track of which movie is being displayed
        var slideIndexCap=1;

        // Adjusts the index of which movie is being displayed
        function plusDivsnew(n) {
          slideIndexCap=slideIndexCap+n;
          showDivsnew(slideIndexCap);
        };

        //Hides other movies and displays the movie as provided by slideIndexCap
        function showDivsnew(n){
          var x = document.getElementsByClassName("slide");
          var i;
          if(n > x.length){
            slideIndexCap=1;
          }
          if(n < 1){
            slideIndexCap=x.length;
          }
          for(i=0; i < x.length; i++){
            if( i == slideIndexCap - 1){
              x[i].style.display = "block";
              x[i].getElementsByClassName("picture")[0].style.display = "block";
            }
            else{
              x[i].style.display = "none";
            }
          }

        };
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body onload="showDivsnew(1);">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-bottom" role="navigation">
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="slide" style="display:none;">
  <div class="row movie-content">
    <div class="col-4">
      <img class="picture movie-tile" src="{poster_image_url}" style="width:auto; height:500px;" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    </div>
    <div class="col-8">
      <div class="row">
        <h1>{movie_title}</h1>
      </div>
      <div class="row">
        <div class="col-8">
          <h2>Genre: {movie_genre}</h3>
        </div>
        <div class="col-4">
          <h2>Rating: {movie_rating} of 10</h3>
        </div>
      </div>
      <div class="row">
        <h2>{movie_storyline}</h2>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-6">
      <a class="arrow_direction"; style="float:left;"onclick="plusDivsnew(-1)">&#10094</a>
    </div>
    <div class="col-6">
      <a class="arrow_direction"; style="float:right;" onclick="plusDivsnew(1)">&#10095</a>
    </div>
  </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_genre=movie.genre,
            movie_rating=movie.rating
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
