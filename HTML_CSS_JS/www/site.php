<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
    echo("Hello World!");
    echo("<h1>Strona Mateusza Sarnowskiego.</h1>");
    echo("<hr>");
    echo("<h2>To jest moja strona.</h2>");
    $characterName = "Mateusz";
    $characterAge = 35;
    echo("There one was a man named $characterName <br>");
    echo("He was $characterAge years old <br>");
    echo("He really liked the name $characterName <br>");
    echo("But didn't like being $characterAge <br>");
    $phrase = "Być albo nie być? Oto jest pytanie.";
    $age = 36;
    $gpa = 3.5;
    $isMale = true;
    $nullVariable = null;
    echo "Fraza to: $phrase <br> Liczba całkowita to: $age <br> GPA to: $gpa <br> Płeć to $isMale <br> Null to: $nullVariable <br>";
    $myName = "Mateusz Matematyk";
    echo "Moje imię to: ".strtolower($myName).". Wielkimi literami: ".strtoupper($myName).". Długość tego ciągu to: ".strlen($myName).".<br>";
    $kamilName = $myName;
    $kamilName = str_replace("Mateusz", "Kamil", $kamilName);
    echo "Mój dobry kumpel, to: ".$kamilName.".<br>";
    echo "Matematyczny ".substr($kamilName, 6, 9)." oraz Informatyczny ".substr($myName, 8, 9).".<br>";
    echo "Wartość bezwzględna z minus sto, to: ".abs(-100).".<br>";
    $twoPowTen = 2**10;
    echo "Dziesiąta potęga dwójki, to: ".pow(2, 10)." ".$twoPowTen.".<br>";
    echo "Pierwiastek kwadratowy z dziesięciu, to: ".sqrt(10).".<br>";
    echo "Pierwiastek kwadratowy z dziesięciu w przybliżeniu do drugiego miejsca po przecinku, to: ".round(sqrt(10), 2).".<br>";
    echo "Maximum z liczby 1 i 2, to: ".max(1,2).".<br>";
    echo "Minimum z liczby 1 i 2, to: ".min(1,2).".<br>";
    echo "Zaokrąglenie w górę liczby 3.3, to: ".ceil(3.3).".<br>";
    echo "Zaokrąglenie w dół liczby 3.9, to: ".floor(3.9).".<br>";
    ?>
    <hr>
    <form action="site.php" method="get">
        Imię: <input type="text" name="name">
        <br>
        Wiek: <input type="text" name="age">
        <br>
        Wyślij: <input type="submit" value="Wyślij">
        <br>
    </form>
    <?php 
    echo "Twoje imię, to: ".$_GET["name"].".<br>";
    echo "Twój wiek, to: ".$_GET["age"].".<br>";
    ?>
    <p>Tutaj zrobimy prosty kalkulator: </p>
    <form action="site.php" method="get">
        <input type="number" step="any" name="num1" id="num1">
        <input type="text" name="binaryOperator" id="binaryOperator">
        <input type="number" step="any" name="num2" id="num2">
        <br>
        <input type="submit" value="Przelicz">
        <br>
    </form>
    <?php 
    if ($_GET["binaryOperator"] == "+") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 + $num2;
        $result = "Wynik dodawania dwóch liczb $num1 i $num2, to: ".$result.".<br>";
    }
    else if ($_GET["binaryOperator"] == "-") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 - $num2;
        $result = "Wynik odejmowania dwóch liczb $num1 i $num2, to: ".$result.".<br>";
    }
    else if ($_GET["binaryOperator"] == "*") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 * $num2;
        $result = "Wynik mnożenia dwóch liczb $num1 i $num2, to: ".$result.".<br>";
    }
    else if ($_GET["binaryOperator"] == "/") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 / $num2;
        $result = "Wynik dzielenia dwóch liczb $num1 i $num2, to: ".$result.".<br>";
    }
    elseif ($_GET["binaryOperator"] == "**") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 ** $num2;
        $result = "Wynik potęgowania dwóch liczb, podstawy $num1 i wykładnika $num2, to: ".$result.".<br>";
    }
    elseif ($_GET["binaryOperator"] == "%") {
        $num1 = $_GET["num1"];
        $num2 = $_GET["num2"];
        $result = $num1 % $num2;
        $result = "Reszta z dzielenia liczby $num1 dzielonej przez $num2, to: ".$result.".<br>";
    }
    else  {
        $result = "Nie podano działania. <br>";
    }
    echo $result;
    ?>
    <br>
    <form action="site.php" method="get">
        Kolor: <input type="text" name="color"> <br>
        Rzeczownik: <input type="text" name="pluralNoun"> <br>
        Osoba: <input type="text" name="celebrity"> <br>
        <input type="submit" value="Wyślij">
    </form>
    <br>
    <br>
    <?php 
    $color = $_GET["color"];
    $pluralNoun = $_GET["pluralNoun"];
    $celebrity = $_GET["celebrity"];
    echo "Róże są $color. <br>";
    echo "$pluralNoun fioletowe. <br>";
    echo "A ja kocham $celebrity. <br>";
    ?>
    <br>
    <form action="site.php" method="post">
        Hasło: <input type="password" name="password" id="password">
        <input type="submit" value="Prześlij hasło!">
    </form>
    <?php 
    echo "Twoje hasło, to: ".$_POST["password"].".<br>";
    ?>
    <br>
    <form action="site.php" method="post">
        <input type="text" name="friend" id="friend">
        <input type="submit" value="Dodaj przyjaciela!">
    </form>
    <?php 
    $friends = array("Mateusz", "Kamil", "Sebastian", "Oskar", "Adam", "Miłosz", "Piotr");
    $friends[count($friends)] = "Joanna";
    $friends[count($friends)] = $_POST["friend"]; 
    sort($friends);
    echo "Moi przyjaciele to: <br>";
    for ($i=0; $i < count($friends); $i++) { 
        echo $friends[$i].".<br>";
    }
    ?>
    <br>
    <?php 
    $friendsWithNumbers = array("Mateusz"=>random_int(0, 100), "Kamil"=>random_int(0, 100), "Sebastian"=>random_int(0, 100), "Oskar"=>random_int(0, 100), "Adam"=>random_int(0, 100), "Miłosz"=>random_int(0, 100), "Piotr"=>random_int(0, 100), "Joanna"=>random_int(0, 100)); 
    ?>
    <form action="site.php" method="post">
        <input type="text" name="student"> <br>
        <input type="submit">
    </form>
    <br>
    <?php
    if (!empty($_POST["student"])) {
        $student = $_POST["student"];
        echo $student." ".$friendsWithNumbers[$student].".<br>";
    } else {
        echo "Nie podano imienia. <br>";
    }
    foreach($friendsWithNumbers as $key => $value){
        echo $key." otrzymał notę: ".$value.".<br>";
    }
    ?>
    <br>
    <form action="site.php" method="post">
        Jabłka: <input type="checkbox" name="fruits[]" value="jabłka" id="apples"> <br>
        Pomarańcze: <input type="checkbox" name="fruits[]" value="pomarańcze" id="oranges"> <br>
        Gruszki: <input type="checkbox" name="fruits[]" value="gruszki" id="pears"> <br>
        <input type="submit">
    </form>
    <?php 
    $fruits = $_POST["fruits"];
    if (!empty($fruits)) {
        echo "Twoje owoce, to: <br>";
        foreach ($fruits as $fruit) { 
            echo $fruit."<br>";
        }
    } else {
        echo "Brak owocków. <br>";
    }
    ?>
    <form action="site.php" method="post">
        Podaj imię: <input type="text" name="userName" id="user-name"> <br>
        <input type="submit" value="Prześlij imię do przywitania się!"> <br>
        Podaj liczbę, która ma być podniesiona do trzeciej potęgi: <input type="number" step="any" name="numberToCube" id="number-three"> <br>
        <input type="submit" value="Podnieś do sześcianu."> <br>
    </form>
    <br>
    <?php 
    function sayHi($name){
        echo "Hello $name <br>";
    }
    function isMale($name){
        if ($name[strlen($name)-1] == "a") {
            echo "Prawdopodobnie jesteś kobietą.<br>"; 
        } else {
            echo "Prawdopodobnie jesteś mężczyzną.<br>";
        }
    }
    $userNameAndIsMale = $_POST["userName"];
    sayHi($userNameAndIsMale);
    isMale($userNameAndIsMale);
    echo "<br>";
    function cube($num){
        return $num * $num * $num;
    }
    $numberToCube = $_POST["numberToCube"];
    echo "Podana liczba $numberToCube powinna być podniesiona do trzeciej potęgi: ".cube($numberToCube).".<br>";
    ?>
</body>
</html>