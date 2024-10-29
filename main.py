<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Usuários</title>
</head>
<body>
    <h1>Cadastro de Usuários</h1>
    <form action="/cadastrar" method="post">
        <label>Nome:</label><input type="text" name="nome"><br>
        <label>Idade:</label><input type="number" name="idade"><br>
        <label>Sexo:</label>
        <select name="sexo">
            <option value="Masculino">Masculino</option>
            <option value="Feminino">Feminino</option>
            <option value="Outro">Outro</option>
        </select><br>
        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>

