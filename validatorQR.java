import java.util.regex.*;
import java.time.LocalDate;

public class ValidadorQR {

    public static void main(String[] args) {

        String codigo = "00101.12345 12345.12345 12345.12345 0000000365";

        String regex = "^\\d{3}\\d{2}\\.\\d{5}\\s\\d{5}\\.\\d{5}\\s\\d{5}\\.\\d{5}\\s(\\d{10})$";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(codigo);

        if (matcher.matches()) {

            String diasStr = matcher.group(1);
            int dias = Integer.parseInt(diasStr);

            LocalDate dataBase = LocalDate.of(2020, 1, 1);
            LocalDate validade = dataBase.plusDays(dias);

            System.out.println("Código válido!");
            System.out.println("Dias: " + dias);
            System.out.println("Data de validade: " + validade);

        } else {
            System.out.println("Código inválido!");
        }
    }
}