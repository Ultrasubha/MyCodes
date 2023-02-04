public class FreedomFighters {
    public static void main(String[] args) {
        String[] freedomFighters1 = { "Subhash Chandra Bose", "Mahatma Gandhi", "Kunwar Singh",
                "Vinayak Damodar Savarkar", "Dadabhai Naoroji", "Tantia Tope", "K. M. Munshi", "Jawaharlal Nehru",
                "Ashfaqulla Khan", "Sardar Vallabhbhai Patel", "Lala Lajpat Rai", "Ram Prasad Bismil",
                "Bal Gangadhar Tilak", "Rani Lakshmi Bai", "Bipin Chandra Pal", "Chittaranjan Das",
                "Begum Hazrat Mahal", "Bhagat Singh", "Lal Bahadur Shastri", "Nana Sahib", "Chandra Shekhar Azad",
                "C. Rajagopalachari", "Abdul Hafiz Mohamed Barakatullah", "Mangal Pandey", "Sukhdev" };
        String[] freedomFighters2 = { "Modiji", "Kangana Ranaut" };

        boolean AchheDin = false;

        if (!AchheDin) {
            System.out.println("Lets take a moment to appreciate the sacrifices of- ");
            for (String v : freedomFighters1)
                System.out.println(v);
            System.out.println(
                    "and many other eminent freedom fighters for creating a secular,democratic and soverign nation of India.");
        } else {
            System.out.println("Lets take a moment to appreciate the sacrifices of- ");
            for (String v : freedomFighters2)
                System.out.println(v);
            System.out.println("for giving freedom to the nation of India on 2014 xD");
        }
        System.out.println("HAPPY REPUBLIC DAY!");
    }
}