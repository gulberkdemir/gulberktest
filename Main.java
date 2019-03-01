package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.ScatterChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;

public class Main extends Application {

    @Override
    public void start(Stage stage) throws Exception{
        //Defining the x axis
        NumberAxis xAxis = new NumberAxis(1960, 2020, 10);
        xAxis.setLabel("Years");

        //Defining the y axis
        NumberAxis yAxis = new NumberAxis   (0, 350, 50);
        yAxis.setLabel("No.of schools");
        yAxis.setAutoRanging(true);

        //Creating the line chart
        //LineChart linechart = new LineChart(xAxis, yAxis);
        ScatterChart<Number, Number> sc = new ScatterChart<>(xAxis, yAxis);
        //Prepare XYChart.Series objects by setting data
        XYChart.Series series = new XYChart.Series();
        series.setName("No of schools in an year");

        series.getData().add(new XYChart.Data(2015, -120));
        series.getData().add(new XYChart.Data(2010, -90));
        series.getData().add(new XYChart.Data(2000, -60));
        series.getData().add(new XYChart.Data(1990, -30));
        series.getData().add(new XYChart.Data(1970, 0));

        //Setting the data to Line chart
        sc.getData().add(series);


        series.getData().add(new XYChart.Data(1990, 30));
        series.getData().add(new XYChart.Data(2000, 60));
        series.getData().add(new XYChart.Data(2010, 90));
        series.getData().add(new XYChart.Data(2015, 120));

        //Setting the data to Line chart
        sc.getData().add(series);
        //Creating a Group object
        Group root = new Group(sc);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 400);

        //Setting title to the Stage
        stage.setTitle("Scatter Chart");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
