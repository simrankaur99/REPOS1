#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
<title>Fish Species Prediction</title>
  <link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
  
</head>

<body>
 <div class="login">
    <form action="{{ url_for('predict')}}"method="post">
        <h1> Fish Species Prediction </h1>
    	Weight : <input type="text" name="Weight" placeholder="Enter the Weight" required="required"/>
        <br><br>
        Length1 : <input type="text" name="Length1" placeholder="Enter the Length1" required="required" />
        <br><br>
		Length2 : <input type="text" name="Length2" placeholder="Enter the Length2" required="required" />
        <br><br>
		Length3 : <input type="text" name="Length3" placeholder="Enter the Length3" required="required" />
        <br><br>
        Height : <input type="text" name="Height" placeholder="Enter the Height" required="required" />
        <br><br>
		Width : <input type="text" name="Width" placeholder="Enter the Width" required="required" />
        <br><br>

        <button type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
        <br><br>
    </form>

<br>
<br>
{{ prediction_text }}

 </div>


</body>
</html>

