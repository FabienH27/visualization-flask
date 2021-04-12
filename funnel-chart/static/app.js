const colorArray = ["#3A86FF","#0CA4A5","#FB4D3D","#3D315B","#36393B","16262e"];

const options = {
    block: {
        dynamicHeight: true,
        minHeight: 20,
        highlight: true,
        fill: {
            type: 'gradient',
            scale: colorArray
        }
    },
    chart: {
        width: window.innerWidth / 3,
        height: window.innerHeight / 2,
        curve: {
            enabled: true
        }
    },
    label: {
        fontFamily: 'Poppins'
    },
    tooltip: {
        enabled: true,
        format: function(label,value) {
            return label + ': ' + value;
        }
    },events: {
        click: {
            block(d) {
                modal.style.display = "block";
                var output = "<span class='close'>&times;</span>" + "<h3 style='color:" + d.fill.raw + "'> Plus d'informations : </h3>" +
                    "<p style='color:" + d.fill.raw + "'>" + d.label.formatted + "</p>" + "<p> Une éventuelle description </p>";
                document.getElementsByClassName("modal-content")[0].innerHTML = output;

                // Get the <span> element that closes the modal
                var span = document.getElementsByClassName("close")[0];

                // When the user clicks on <span> (x), close the modal
                span.onclick = function() {
                modal.style.display = "none";
                }
            },
        },
    },
};

var funnelArray = [];
var output = "";
var rbs;

$( document ).ready(function() {
    initiateFunnel();
    generateFunnel();
    
    $("input[type='radio'][name='funnel']").on('change',function(){
        generateFunnel();
    });    
});

function initiateFunnel(){
    for (let i = 0; i < data.length; i++) {
        var div = document.createElement('div');
        div.id = "funnel" + (i+1);
        document.getElementById("container").appendChild(div);
        const funnelTemp = new D3Funnel('#funnel' + (i+1));
        funnelArray.push(funnelTemp);
    }
    for (let i = 0; i < data.length; i++) {
        datalist = data[i];
        output += '<div><input type="radio" value="'+ datalist[0] +'" name="funnel">' + datalist[0] +'</input></div>';
        document.getElementById("radios").innerHTML = output;
    }
    rbs = document.querySelectorAll("input[name='funnel']");
    rbs[0].checked = true;
}

function generateFunnel(){
    let selectedFunnel;
    for(const rb of rbs){
        if(rb.checked){
            selectedFunnel = rb.value;
            break;
        }
    }
    for(let i = 0; i < funnelArray.length; i++){
        if(selectedFunnel == funnelArray[i].container.id){
            clearFunnel(funnelArray);
            funnelArray[i].draw(data[i][1],options);
        }
    }
}

function clearFunnel(div){
    div.forEach(element => 
        d3.select("#" + element.container.id).selectAll('svg').remove());
}

var modal = document.getElementById("myModal");

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
    modal.style.display = "none";
    }
}
