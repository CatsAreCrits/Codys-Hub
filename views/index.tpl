<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Meta -->
        <title>Cody's Hub</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Cody Morton">
        <meta name="robots" content="noindex, nofollow">
        <!-- CSS -->
        <link href="http://catsarecrits.com/hub1/assets/css/animate.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/bootstrap.min.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/flat-ui-pro.min.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/style.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="navbar-text navbar-right">
                <span id="time"></span>
                <span class="date">{{get('date')}}</span>
                <span class="links"><a target="_new" href="https://www.google.com/search?q=weather">Weather</a></div>
            </div>
                <div class="holdings navbar-text navbar-left">
                    <p class="day_change">Today's Change: <span id="percentChange"
                    %if not "-" in day_change_percent:
                        class="positive"
                        %elif "-" in day_change_percent:
                        class="negative"
                        %else:
                        class="no_change"
                        %end
                    >{{get('day_change_percent')}}</span> | <span id="dollarChange">{{get('day_change_dollar')}}</span></p>
                    <p class="total_change">Total Gain: <span id="percentChange"
                        %if not "-" in total_change_percent:
                        class="positive"
                        %elif "-" in total_change_percent:
                        class="negative"
                        %else:
                        class="no_change"
                        %end
                    >{{get('total_change_percent')}}</span> | <span id="dollarChange">{{get('total_change_dollar')}}</span></p>
                </div>
                <div class="holdings navbar-text navbar-left">
                    <p id="value">{{get('holdings')}}</p>
                </div>
            </nav>
            <div id="quicklinks">
                <div class="well">
                    <div class="row text-center">
                        <div class="col-lg-2"><a class="button" href="http://www.facebook.com"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/facebook.png" alt="test"></a></div>
                        <div class="col-lg-2"><a class="button" href="http://stocktwits.com/"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/stocktwits.png" width="128px" height="128px"></a></div>
                        <div class="col-lg-2"><a class="button" href="http://www.reddit.com"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/reddit.png"></a></div>
                        <div class="col-lg-2"><a class="button" href="http://www.twitter.com"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/twitter.png"></a></div>
                        <div class="col-lg-2"><a class="button" href="https://play.google.com/music/listen"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/gmusic.png"></a></div>
                        <div class="col-lg-2"><a class="button" href="http://www.netflix.com/"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/netflix.png"></a></div>
                    </div>
                </div>
            </div>
            <div class="container">
            </div>
        </body>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script src="http://catsarecrits.com/hub1/assets/js/bootstrap.min.js"></script>
        <script src="http://catsarecrits.com/hub1/assets/js/js.js"></script>
    </html>