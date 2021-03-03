<!DOCTYPE html>
<html>
    <head>
        <title>IHM Mr BONVENT</title>
        <link rel="icon" type="image/png" href="images/favicon.png"/>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/picnic">
        <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="css/style.css">
        <script src="https://kit.fontawesome.com/d5091b0680.js" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>
        <script src="js/script.js"></script>
        <script src="js/switch.js"></script>
    </head>
    
    
    <body data-spy="scroll" data-target=".navbar" data-offset="60">
        
        <nav class="navbar navbar-default navbar-fixed-top">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                         <span class="icon-bar"></span>
                         <span class="icon-bar"></span>
                         <span class="icon-bar"></span>
                    </button>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav">
                        <li><a href="#presentation">Présentation</a></li>
                        <li><a href="#parametres">Paramètres</a></li>
                        <li><a href="#etat">Etat du PS</a></li>
                        <li><a href="#historique">Historique</a></li>
                    </ul>
                </div>        
        </nav>
       
        <section id="home" class="container-fluid">
            <div class="heading">
                <h1 class="color2">Bienvenue Mr BONVENT</h1>
                <div>
                    <h3>Ceci est votre interface de visualisation pour votre panneau solaire</h3>
                </div>
            </div>
        </section>
        
        
        <section id="presentation">
            <div class="gray-divider"></div>
            <div class="heading">
                <h2>Présentation</h2>
            </div>
            <div class="container">
                <div class="col-md-4">
                    <h3>
                        <i class="fas fa-leaf color1"></i> 
                        Qu'y a t-il sur cette IHM ?
                    </h3>
                    <h5>Sur cette IHM, vous pourrez consulter :</h5>
                    <ul>
                        <li>La direction du vent</li>
                        <li>La vitesse du vent</li>
                        <li>La valeur des rafales</li>
                        <li>L'état de votre panneau solaire</li>
                        <li>Un historique avec toutes ces données</li>
                    </ul>
                </div>
                <div class="col-md-4" style="text-align: center">
                    <img src="images/panneau.png" alt="Panneau Solaire" class="img-circle" style="width: 60%">
                </div>
                <div class="col-md-4">
                    <h3>
                        <i class="fas fa-search color1"></i> 
                        Où se trouve le panneau solaire ?
                    </h3>
                    <h5>Le panneau solaire se situe sur l'Ïle d'Yeu (Vendée).</h5>
                    <img src="images/ileyeu.png" alt="Ile d'Yeu" style="width: 70%; margin-left: auto; margin-right: auto; display: block;">
                </div>
            </div>
        </section>
        
        <?php
            $tab = file('donnees/'.date("Y-m-d").'.csv');            
            /*Quelle ligne doit-on lire ?*/
            /*1h, 4h, 7h, 10h, 13h, 16h, 19h et 22h*/

            if(date("H") >= 0 && date("H") < 4) {
                $prem_ligne = $tab[0];
                $linktext = explode(",", $prem_ligne);
                if(linktext[6] > 360) {
                    $linktext[6] -= 360;
                }
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 4 && date("H") < 7) {
                $deux_ligne = $tab[1];
                $linktext = explode(",", $deux_ligne);
                if($linktext[6] > 360) {
                    $linktext[6] -= 360;
                }
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 7 && date("H") < 10) {
                $trois_ligne = $tab[2];
                $linktext = explode(",", $trois_ligne);
                if($linktext[6] > 360) {
                    $linktext[6] -= 360;
                }
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 10 && date("H") < 13) {
                $quat_ligne = $tab[3];
                $linktext = explode(",", $quat_ligne);
                if($linktext[6] > 360) {
                    $linktext[6] -= 360;
                }
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
                print_r(fgetcsv($file));
                fclose($file);
            } elseif(date("H") >= 13 && date("H") < 16) {
                $cinq_ligne = $tab[4];
                $linktext = explode(",", $cinq_ligne);
				if($linktext[6] > 360) {
					$linktext[6] -= 360;
				}
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 16 && date("H") < 19) {
                $sixi_ligne = $tab[5];
                $linktext = explode(",", $sixi_ligne);
				if($linktext[6] > 360) {
					$linktext[6] -= 360;
				}
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 19 && date("H") < 22) {
                $sept_ligne = $tab[6];
                $linktext = explode(",", $sept_ligne);
                if($linktext[6] > 360) {
					$linktext[6] -= 360;
				}
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            } elseif(date("H") >= 22 && date("H") < 24) {
                $huit_ligne = $tab[7];
                $linktext = explode(",", $huit_ligne);
				if($linktext[6] > 360) {
					$linktext -= 360;
				}
                $direction = $linktext[6];
                $directionText = "";
                $vitvent = $linktext[5];
                $vitrafale = $linktext[4];
            }
        
            if($direction >= 0 && $direction < 45) {
                $directionText = "Nord";
            } elseif ($direction >= 45 && $direction < 90) {
                $directionText = "Nord-Est";
            } elseif ($direction >= 90 && $direction < 135) {
                $directionText = "Est";
            } elseif ($direction >= 135 && $direction < 180) {
                $directionText = "Sud-Est";
            } elseif ($direction >= 180 && $direction < 225) {
                $directionText = "Sud";
            } elseif ($direction >= 225 && $direction < 270) {
                $directionText = "Sud-Ouest";
            } elseif ($direction >= 270 && $direction < 315) {
                $directionText = "Ouest";
            } elseif ($direction >= 315 && $direction < 360) {
                $directionText = "Nord-Ouest";
            } else ($direction > 360) {
                $directionText = "Inconnue"
            }
        ?>
        
        <section id="parametres">
        
            <div class="container">
                <div class="white-divider"></div>
                <div class="heading">
                    <h2>Paramètres du vent</h2>
                </div>
                <ul class="timeline" style="list-style: none;">
                    <li>
                        <div class="timeline-badge"><span class="fas fa-compass"></span></div>
                        <div class="timeline-panel-container">
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h3>Direction du vent</h3>
                                    <h5>Le vent souffle en direction</h5>
                                    <h4><?php echo $directionText; ?> (<?php echo $direction; ?>°)</h4>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="timeline-badge"><span class="fas fa-stopwatch"></span></div>
                        <div class="timeline-panel-container-inverted">
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h3>Vitesse du vent</h3>
                                    <h5>Le vent souffle à une vitesse de</h5>
                                    <h4><?php echo $vitvent; ?> km/h</h4>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="timeline-badge"><span class="fas fa-wind"></span></div>
                        <div class="timeline-panel-container">
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h3>Vitesse des rafales</h3>
                                    <h5>Le rafales de vent soufflent à une vitesse de</h5>
                                    <h4><?php echo $vitrafale; ?> km/h</h4>
                                </div>
                            </div>
                        </div>
                    </li>
                
                </ul>
            </div>
            
        </section>
                
        <section id="etat">
            <div class="container">
                 <div class="gray-divider"></div>
                <div class="heading">
                    <h2>Etat du Panneau Solaire</h2>
                </div>
                <div class="col-md-12">
                    <h4>Le panneau solaire est</h4>
                    <label class="switch">
                      <input type="checkbox">
                      <div class="slider"></div>
                    </label>
                    <h1 id="etatSwitch" class="color1">Non sécurisé</h1>
                    <h4 id="txtSitu">Je souhaite mettre le panneau en mode</h4>
                    <br>
                    <form method="post">
                        <button id="manuel" name="manuel">Sécurisé (0°)</button>
                        <button id="automatique" name="automatique">Automatique</button>
                    </form>
                    <?php
                        if(array_key_exists('manuel', $_POST)) { 
                            manuel(); 
                        } 
                        else if(array_key_exists('automatique', $_POST)) { 
                            automatique();
                        } 
                        function manuel() { 
                            echo "";
                            
                        } 
                        function automatique() { 
                            echo "";
                            
                        }
                    ?>
                </div>
            </div>
        </section>
        
        <section id="historique">
            <div class="container">
                <div class="white-divider"></div>
                <div class="heading">
                    <h2>Historique</h2>
                </div>
                <canvas id="chart" width="800" height="450"></canvas>
                <script type="text/javascript">
                    chartIt();

            async function chartIt() {
                const data = await getData();
                const ctx = document.getElementById('chart').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.xsvitss,
                        datasets: [{
                            label: "Etat du panneau",
                            data: data.ysetat,
                            borderColor: "#333333",
                            fill: false
                        },
                        {
                            label: "Vitesse du vent",
                            data: data.ysvitss,
                            borderColor: "#0FEB9E",
                            fill: false
                        },
                        {
                            label: "Vitesse des rafales",
                            data: data.ysvitssraf,
                            borderColor: "#3e95cd",
                            fill: false
                        }]
                    },
                });
            }

            async function getData() {
                <?php
                    $date = date("Y-m-d"); //Récupération date d'aujourd'hui
                    //$datehier = date("Y-m-d", strtotime($date." - 1 days"));
                ?>

                const xsetat = []; //Tableau des gradations sur l'axe X
                const ysetat = []; //Tableau des gradations sur l'axe Y

                const xsvitss = []; //Tableau des gradations sur l'axe X
                const ysvitss = []; //Tableau des gradations sur l'axe Y
                
                const xsvitssraf = []; //Tableau des gradations sur l'axe X
                const ysvitssraf = []; //Tableau des gradations sur l'axe Y

                const response = await fetch('<?php echo "donnees/$date" ?>.csv'); //Lecture du fichier des données
                const data = await response.text();
				
				const responseetat = await fetch('<?php echo "donnees/$date" ?>-etats.csv'); //Lecture du fichier des données
				const dataetat = await responseetat.text();

                const table = data.split('\n').slice(0);
				const tableetat = dataetat.split('\n').slice(0);
				
                table.forEach(row => {
                    const columns = row.split(',');

                    const heure = columns[3]; //Récupération de la valeur de l'heure
                    const mois = columns[1];

                    xsetat.push(parseFloat(heure) + "h"); //Gradation graphique sur l'axe X
                    xsvitss.push(parseFloat(heure) + "h"); //Gradation graphique sur l'axe X

                    //const etat = columns[4]; //Récupération de la valeur de l'état du panneau
                    const vitss = columns[5]; //Récupération de la valeur de la vitesse du vent
                    const vitssraf = columns[3]; //Récupération de la valeur de la vitesse des rafales de vent

                    //ysetat.push(etat); //Gradation graphique sur l'axe Y
                    ysvitss.push(vitss); //Gradation graphique sur l'axe Y
                    ysvitssraf.push(vitssraf); //Gradation graphique sur l'axe Y
                });
				tableetat.forEach(row => {
                    const columns = row.split(',');
					const etat = columns[0]; //Récupération de la valeur de l'état du panneau
					ysetat.push(etat); //Gradation graphique sur l'axe Y
				});
					
                return { xsetat, ysetat, xsvitss, ysvitss, xsvitssraf, ysvitssraf };
            }
                </script>
            </div>
            
        </section>
        
        <footer class="text-center">
            <a href="#home">
                <span class="glyphicon glyphicon-chevron-up"></span>
            </a>
            <h5>© 2021 <br> GRISVAL Thibault <br> CHARPY Valentin <br> BAILO Thomas </h5>
            <h5>Les données météo proviennent du site <a href="www.infoclimat.fr">www.infoclimat.fr</a></h5>
        </footer>
        <script src="js/menu.js"></script>
        
    </body>

</html>
