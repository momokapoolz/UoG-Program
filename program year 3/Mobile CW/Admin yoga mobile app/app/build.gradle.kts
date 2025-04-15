plugins {
    alias(libs.plugins.android.application)
    id("com.google.gms.google-services")

}

android {
    namespace = "com.example.adminyogaappcw"
    compileSdk = 35 // Changed to latest stable SDK version

    defaultConfig {
        applicationId = "com.example.adminyogaappcw"
        minSdk = 24
        targetSdk = 34 // Changed to match compileSdk
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17 // Updated to a newer Java version
        targetCompatibility = JavaVersion.VERSION_17
    }

    // Optional: Enable ViewBinding if needed
    buildFeatures {
        viewBinding = true
    }
}

dependencies {
    implementation(libs.appcompat)
    implementation(libs.material)
    implementation(libs.activity)
    implementation(libs.constraintlayout)
    testImplementation(libs.junit)
    androidTestImplementation(libs.ext.junit)
    androidTestImplementation(libs.espresso.core)

     // hoặc version mới hơn


    // Firebase BoM (Bill of Materials)
    implementation(platform("com.google.firebase:firebase-bom:33.12.0"))

    // Firebase Analytics
    implementation("com.google.firebase:firebase-analytics")

    // Firebase Firestore (Add this for Firestore database)
    implementation("com.google.firebase:firebase-firestore")

    // Firebase Authentication (if needed)
    implementation("com.google.firebase:firebase-auth")

    implementation ("com.google.firebase:firebase-database:20.3.0")


}