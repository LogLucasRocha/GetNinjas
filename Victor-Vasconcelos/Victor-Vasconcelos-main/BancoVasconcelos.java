/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package banco.vasconcelos;

import java.util.Scanner;
import javax.lang.model.SourceVersion;


/**
 *
 * @author lucasrocha
 */
public class BancoVasconcelos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    }

    @Override
    public SourceVersion getSupportedSourceVersion() {
        return SourceVersion.latest();
    }
}

class Cliente{
    private String nome;
    private String sobrenome;
    private String cpf;
    private double saldo;
    
    public Cliente(String nome, String sobrenome, String cpf){
    this.nome = nome;
    this.sobrenome = sobrenome;
    this.cpf = cpf;
    this.saldo = 0.0;
    }
    
    //Métodos de classe Cliente
    public void consultarSaldo() {
        System.out.println("Seu saldo atual é R$" + saldo);
    }// fim método consultarSaldo
    
    public void depositar(double valor){
    if (valor > 0){
      saldo += valor;
      System.out.println("Depósito de R$" + valor + " realizado com sucesso.");
    } else {
        System.out.println("Valor de depósito inválido");}
    } // fim método depositar
     
    public void sacar (double valor){
    if (valor > 0 && valor <= saldo){
    saldo -= valor;
    System.out.println("Saque de R$" + valor + " realizado com sucesso.");
    } else {
    System.out.println("Saldo insuficiente ou valor de saque inválido.");} 
    } //fim método sacar
}//fim classe cliente

public class Banco{
    public static void main (String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informe seu nome por favor: ");
        String nome = scanner.nextLine();
        System.out.println("Informe seu sobrenome por favor: ");
        String sobrenome = scanner.nextLine();
        System.out.println("Informe seu CPF por favor: ");
        String cpf = scanner.nextLine();
        //instanciando um objeto da classe Cliente
        Cliente cliente = new Cliente(nome, sobrenome, cpf);
        
        boolean continuar = true;
        while(continuar) {
            System.out.println("\n0 que deseja: ");
            System.out.println("1 - Consultar saldo");
            System.out.println("2 - Fazer depósito");
            System.out.println("3 - Fazer saque");
            System.out.println("4 - Encerrar aplicação\n\n");
                    
            int escolha = scanner.nextInt();
            switch (escolha) {
                case 1:
                    cliente.consultarSaldo();
                    break;
                case 2:
                    System.out.println("Informe o valor a ser depositado");
                    double valorDepositado = scanner.nextDouble();
                    cliente.depositar(valorDepositado);
                    break;
                case 3:
                    System.out.println("Informe o valor a ser sacado:");
                    double valorSaque = scanner.nextDouble();
                    cliente.sacar(valorSaque);
                    break;
                case 4:
                    continuar = false;
                    System.out.println("Encerrando a aplicação, até breve.");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        }
        scanner.close();
         
    }    
}
