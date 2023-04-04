using OpenQA.Selenium;
using Selenium.Extensions;
using Selenium.WebDriver.UndetectedChromeDriver;
using System.Xml.Linq;



namespace BOTVA
{
    

    public partial class Form1 : Form

    {
        public UndetectedChromeDriver? driver;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            driver = (UndetectedChromeDriver?)UndetectedChromeDriver.Instance("BOTVA");
            label1.Text = "0";

            try
            {
                driver.GoTo("https://g1.botva.ru");
                driver.FindElement(By.ClassName("sign_in")).Click();
                driver.FindElement(By.Name("email")).Clear();
                driver.FindElement(By.Name("email")).SendKeys("123");
                driver.FindElement(By.Name("password")).Clear();
                driver.FindElement(By.Name("password")).SendKeys("123");
            }
            catch
            {
                button1.Text = "NO LOGIN";
                textBox1.Text = textBox1.Text + "NO LOGIN \n";
            }
            finally
            {

            }
            //////////////////////////////////////////////////////
            driver.GoTo("https://g1.botva.ru/monster.php?a=monsterpve");
            do
            {
                try
                {

                    driver.FindElement(By.XPath("/html/body/div[5]/div[3]/div[2]/div[2]/div[2]/div[4]/form/input[3]")).Click();
                    button1.Text = "good";
                    textBox1.Text = textBox1.Text + "good \n";
                    label1.Text = "1";
                }
                catch
                {
                    button1.Text = "NOT FOUND";
                    textBox1.Text = textBox1.Text + "NOT FOUND \n";
                    for (int i = 0; i < 100; i++)
                    {
                        System.Threading.Thread.Sleep(50);
                        Application.DoEvents();
                    }
                    label1.Text = "0";
                }
                finally
                {
                    //System.Threading.Thread.Sleep(5000);
                }
                driver.Refresh();
            }
            while (label1.Text == "0");
            ////driver.stop

            driver.Close();
            driver.Quit();



        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "1";
            driver.Close();
            driver.Quit();
        }
    }
}