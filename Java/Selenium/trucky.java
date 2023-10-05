package trukky;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

import java.util.concurrent.TimeUnit;

public class auto {
    public static void main(String[] args) {

        System.setProperty("webdriver.edge.driver","C:\\SeleniumProj\\setup\\edgedriver_win64\\msedgedriver.exe");
        WebDriver driver1 = new EdgeDriver();
        driver1.manage().window().maximize();
        driver1.get("https://www.trukky.com/door-to-door-goods-delivery");
        Actions action=new Actions(driver1);

        String url = driver1.getCurrentUrl();
        String pageTitle = driver1.getTitle();
        System.out.println("URL: " + url + "Page Title: " + pageTitle);

        try {
            Thread.sleep(5000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        WebElement pickupCity = driver1.findElement(By.xpath("//input[@placeholder='Enter pickup city']"));
        pickupCity.sendKeys("Hyderabad");
        driver1.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/ul[1]/li[1]")).click();

        WebElement dropCity = driver1.findElement(By.xpath("//input[@placeholder='Enter drop city']"));
        dropCity.sendKeys("Delhi");
        driver1.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[1]")).click();

        WebElement checkPrice = driver1.findElement(By.xpath("//button[normalize-space()='Check price']"));
        checkPrice.click();

        try {
            Thread.sleep(5500);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        driver1.findElement(By.xpath("(//div[@class='jsx-665002787 serviceDetails'])[2]")).click();

        try {
            Thread.sleep(3000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        driver1.findElement(By.xpath("(//div[@class='jsx-665002787 serviceDetails'])[1]")).click();

        try {
            Thread.sleep(3500);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        driver1.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]")).click();

        try {
            Thread.sleep(2000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        Select chooseMaterialDropdown = new Select(driver1.findElement(By.xpath("(//select[@class='jsx-1905266029'])[1]")));
        chooseMaterialDropdown.selectByVisibleText("Window AC");

        driver1.findElement(By.xpath("(//input[@placeholder='Enter No. of item'])[1]")).sendKeys("2");

        WebElement forwardButton = driver1.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]"));
        forwardButton.click();

        try {
            Thread.sleep(2000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        driver1.findElement(By.xpath("(//button[normalize-space()='Next'])[1]")).click();

        try {
            Thread.sleep(3000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        WebElement dateselect = driver1.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[19]/abbr[1]"));
        dateselect.click();

        nextButton = driver1.findElement(By.xpath("(//button[normalize-space()='Next'])[1]"));
        nextButton.click();

        try {
            Thread.sleep(2000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        WebElement phoneInput = driver1.findElement(By.xpath("(//input[@placeholder='Whatsapp no. recommended'])[1]"));
        phoneInput.sendKeys("6397903211");

        WebElement getprice = driver1.findElement(By.xpath("(//button[normalize-space()='Get price'])[1]"));
        getprice.click();
    }
}