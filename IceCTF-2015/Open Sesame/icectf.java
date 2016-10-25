import java.io.PrintStream;

public class icectf
{
    public static String[] arr = { "root", "ssh", "pragma", "memory", "gcc", "malloc", "compile", "packet", "reverse", "stack", "grep", "icectf", "system", "cache", "hack", "backdoor", "fail", "regex", "default", "class", "rsa", "foo", "engineer", "tarball", "void", "unix", "/dev/null" };

    public static void main(String[] paramArrayOfString) {
        try {
            if ((paramArrayOfString[0].charAt(0) == 'f') && (paramArrayOfString[0].charAt(1) == 'l') && (paramArrayOfString[0].charAt(2) == 'a') && (paramArrayOfString[0].charAt(3) == 'g'))
            {
                System.out.println("Checkpoint 1");
                if (funky_func(paramArrayOfString[0]))
                {
                    System.out.println("Checkpoint 2");
                    if (funkier_func(paramArrayOfString[0]))
                    {
                        System.out.println("Checkpoint 3");
                        if (funkiest_func(paramArrayOfString[0]))
                        {
                            System.out.println("Congratulations!");
                            System.out.println("Flag: " + paramArrayOfString[0]);
                        }
                        else {
                            throw new Exception();
                        }
                    }
                    else throw new Exception();
                }
                else
                    throw new Exception();
            }
            else
                throw new Exception();
        }
        catch (Exception localException)
        {
            System.out.println("PWNZ0R'D 1N TH3 PH4CE!!1");
        }
    }

    public static boolean funky_func(String paramString)
    {
        for (int i = 11; i > 0; i--)
        {
            if (i % 8 == 0)
            {
                if (paramString.split("_")[1].equals(arr[i]))
                    return true;
            }
        }
        return false;
    }

    public static boolean funkier_func(String paramString)
    {
        int i = 5;
        while (i <= 22)
        {
            if ((i % 2 == 0) && (arr[i].charAt(0) == 'e'))
                return arr[i].equals(paramString.split("_")[2]);
            i++;
        }
        return false;
    }

    public static boolean funkiest_func(String paramString)
    {
        return paramString.split("_")[3].equals(arr[11]);
    }
}
