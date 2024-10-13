<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect input
    $old_password = $_POST['old_password'];
    $new_password = $_POST['new_password'];
    $confirm_password = $_POST['confirm_password'];
    if ($new_password !== $confirm_password) {
        header("Location: change-password.html?error=New passwords do not match.");
        exit();
    }
    $user_data = json_decode(json: file_get_contents(filename: 'data.json'), associative: true);
        $user_data['password'] = $new_password;
    file_put_contents(filename: 'data.json', data: json_encode( value: $user_data, flags: JSON_PRETTY_PRINT));
    header("Location: change-password.html?error=Password changed successfully.");
    exit();
}
?>