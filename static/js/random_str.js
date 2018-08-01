String.prototype.hexEncode = function(){
    var hex, i;

    var result = "";
    for (i=0; i<this.length; i++) {
        hex = this.charCodeAt(i).toString(16);
        result += ("000"+hex).slice(-4);
    }

    return result
};

String.prototype.hexDecode = function(){
    var j;
    var hexes = this.match(/.{1,4}/g) || [];
    var back = "";
    for(j = 0; j<hexes.length; j++) {
        back += String.fromCharCode(parseInt(hexes[j], 16));
    }

    return back;
};

function random_str(len, join) {
    len = len || 10;
    if (typeof join === 'undefined') {
        join = true;
    }
    var str_set = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)';
    var random = [];

    for (var i = 0; i < len; i++) {
        random = (new Array(len)).fill(0).map(function(_){
            return str_set.charAt(Math.floor(Math.random()*str_set.length));
        })
    }

    return join ? random.join('') : random;
}

function strToHexArray(str) {
    return Array.prototype.map.call(str, function(x){ return parseInt(x.hexEncode(), 16); })
}

function encode32(str) {
    var encoder = new base32.Encoder();
    return encoder.write(strToHexArray(str)).finalize();
}

function decode32(str) {
    var decoder = new base32.Decoder();
    return decoder.write(str).finalize().map(function(x){
        return x.toString(16).hexDecode()
    }).join('');
}
