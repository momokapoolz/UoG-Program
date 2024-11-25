<?php

function query($pdo, $sql, $parameters = [])
{
    $query = $pdo->prepare($sql);
    $query->execute($parameters);
    return $query;
}

//login function
function login($pdo, $username, $password)
{
    $sql = "SELECT * FROM user WHERE username = :username AND password = :password";
    $stm = $pdo->prepare($sql);
    $stm->bindValue(':username', $username);
    $stm->bindValue(':password', $password);
    $stm->execute();
    return $stm->fetchAll();
}

//register function
function register($pdo, $username, $password, $email)
{
    $sql = "INSERT INTO user SET username = :username, password = :password, email = :email";
    $stm = $pdo->prepare($sql);
    $stm->bindValue(':username', $username);
    $stm->bindValue(':password', $password);
    $stm->bindValue(':email', $email);
    $stm->execute();
}

//delete question
function delete_question($pdo, $id)
{
    $parameters = [':id' => $id];
    $sql = 'DELETE FROM questions WHERE id = :id';
    query($pdo, $sql, $parameters);
}

//edit question
function edit_question($pdo, $question_text, $id)
{
    $parameters = [':id' => $id];
    $sql = "UPDATE questions SET question_text = :question_text WHERE id = :id";
    $parameters = [':question_text' => $question_text, ':id' => $id];
    query($pdo, $sql, $parameters);
}


//insert question
function insert_question($pdo, $question_text, $fileToUpload, $user_id)
{
    $sql = 'INSERT INTO questions (question_text, question_date, `questionimage`, user_id) VALUES (:question_text, CURDATE(), :fileToUpload, :user_id)';
    $parameters = [':question_text' => $question_text, ':fileToUpload' => $fileToUpload, ':user_id' => $user_id];
    query($pdo, $sql, $parameters);
}



function list_question($pdo)
{
    $sql = 'SELECT questions.id, questions.question_text, questions.question_date, questions.questionimage, questions.user_id, user.username, user.email
    FROM questions
    INNER JOIN user ON user_id  = user.id';
    $return = query($pdo, $sql);
    return $return->fetchALL();
}


function list_answer($pdo, $id)
{   
    $sql = 'SELECT *
    FROM answer
    WHERE question_id = :id';
    $parameter = [':id' => $id];
    $return = query($pdo, $sql, $parameter);
    return $return->fetchAll();
}


//insert answer
function insert_answer($pdo, $answer_text, $question_id)
{
    $sql = 'INSERT INTO answer (answer_text, answer_date, question_id) VALUES (:answer_text, CURDATE(), :question_id)';

    $parameters = [':answer_text' => $answer_text, ':question_id' => $question_id];
    query($pdo, $sql, $parameters);
}