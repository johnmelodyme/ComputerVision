package my.kylogger.johnmelodyme.iot.embedded.machinelearning.facialrecognition;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import org.opencv.android.CameraBridgeViewBase;
import org.opencv.core.Mat;

public class FacialRecognitionActivity extends AppCompatActivity implements CameraBridgeViewBase.CvCameraViewListener {
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

    @Override
    public void onCameraViewStarted(int width, int height) {

    }

    @Override
    public void onCameraViewStopped() {

    }

    @Override
    public Mat onCameraFrame(Mat inputFrame) {
        return null;
    }
}
