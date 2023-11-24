document.querySelector("#gradForm").forEach(
	function(rad)
  {
  	rad.onchange = function()
    {
      if(document.getElementById("queries") == "findAllGradRates")
      {
        document.getElementById("parameters_findAll").style.display = "block";
      }
  	}
});