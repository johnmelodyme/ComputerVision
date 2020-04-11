package my.kylogger.johnmelodyme.iot.embedded.machinelearning.facialrecognition;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class FacialRecognitionActivity extends AppCompatActivity {
    public static final String TAG = "FacialRecognition";

    public void DeclarationInit() {

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "Launching " + FacialRecognitionActivity.class.getSimpleName());
        DeclarationInit();
    }
}
