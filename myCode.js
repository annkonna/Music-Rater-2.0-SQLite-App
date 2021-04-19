
function songsCallback(response){
    var songs = JSON.parse(response);
    var to_html = ""
    for(var song_id in songs){
        var song = songs[song_id];
        // song.title
        // song.artist
        // song.ratings
        to_html = to_html + "<a href=\"https://www.youtube.com/watch?v=" + song_id + "\" target=\"_blank\">"
        to_html = to_html + song.title + " - " + song.artist + "</a><br/>";
        to_html = to_html + song.ratings + "<br/>";
        to_html = to_html + "Rate: ";
        for(var i=1; i<=5; i=i+1){
            to_html = to_html + "<button onClick=\"rate(\'" + song_id + "\', " + i + ")\">"+i+"</button>";
        }
        to_html = to_html + "<hr/>";
    }
    console.log(to_html);
    document.getElementById("songs").innerHTML = to_html;
}

function getSongs(){
    ajaxGetRequest("songs", songsCallback);
}


function newSong(){
    song_id = document.getElementById("song_id_input").value;
    title = document.getElementById("song_title_input").value;
    artist = document.getElementById("song_artist_input").value;
    
    document.getElementById("song_id_input").value = "";
    document.getElementById("song_title_input").value = "";
    document.getElementById("song_artist_input").value = "";
    
    song = {"song_id": song_id, "title": title, "artist": artist};
    song = JSON.stringify(song);
    ajaxPostRequest("add_song", song, songsCallback)
}

function rate(song_id, rating){
    songRating = {"song_id": song_id, "rating": rating};
    songRating = JSON.stringify(songRating);
    ajaxPostRequest("rate_song", songRating, songsCallback)
}


function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}


function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}
