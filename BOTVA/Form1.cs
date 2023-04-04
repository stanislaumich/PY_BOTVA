using Selenium.WebDriver.UndetectedChromeDriver;

namespace BOTVA
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (var driver = UndetectedChromeDriver.Instance("BOTVA"))
            {
                driver.GoTo("https://google.com");
                try
                driver.FindElement("css selector", "uy");
                
            }
        }
    }
}