$(document).ready(function() {
     if (window.location.protocol == "https:") {
      var ws_scheme = "wss://";
    } else {
      var ws_scheme = "ws://"
    };

    let socket = io.connect(ws_scheme + location.host);
});
