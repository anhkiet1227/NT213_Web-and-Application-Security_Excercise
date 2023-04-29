package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    // Declare variables
    EditText username, password, repassword;
    Button signup, signin;
    DBHelper DB;

    // Create the activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Call the parent constructor
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username = (EditText) findViewById(R.id.username);
        password = (EditText) findViewById(R.id.password);
        repassword = (EditText) findViewById(R.id.repassword);
        signup = (Button) findViewById(R.id.btnsignup);
        signin = (Button) findViewById(R.id.btnsignin);
        DB = new DBHelper(this);

        signup.setOnClickListener(new View.OnClickListener() {
            // When the user clicks the sign up button
            @Override
            public void onClick(View view) {
                // Get the username and password
                String user = username.getText().toString();
                String pass = password.getText().toString();
                String repass = repassword.getText().toString();

                if (user.equals("") || pass.equals("") || repass.equals(""))
                    // Check if the username and password are empty
                    Toast.makeText(MainActivity.this, "Please enter all the fields", Toast.LENGTH_SHORT).show();
                else {
                    if (pass.equals(repass)) {
                        // Check if the username is already taken
                        Boolean checkuser = DB.checkusername(user);
                        if (checkuser == false) {
                            // If the username is not taken, insert the username and password into the database
                            Boolean insert = DB.insertData(user, pass);
                            if (insert == true) {
                                // If the username and password are inserted successfully, go to the login activity
                                Toast.makeText(MainActivity.this, "Registered successfully", Toast.LENGTH_SHORT).show();
                                Intent intent = new Intent(getApplicationContext(), LoginActivity.class);
                                startActivity(intent);
                            } else {
                                // If the username and password are not inserted successfully, show an error message
                                Toast.makeText(MainActivity.this, "Register fail", Toast.LENGTH_SHORT).show();
                            }
                        } else {
                            // If the username is taken, show an error message
                            Toast.makeText(MainActivity.this, "Register again", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        // If the passwords do not match, show an error message
                        Toast.makeText(MainActivity.this, "Passwords not matching", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });

        signin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // If the user clicks the sign in button, go to the login activity
                Intent intent = new Intent(getApplicationContext(), LoginActivity.class);
                startActivity(intent);
            }
        });
    }
}
