/*


    PRÁCTICA 2 (PARTE 2): ESPECIFICACIÓN Y VERIFICACIÓN DE ALGORITMOS ITERATIVOS EN DAFNY

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: IRIONDO DELGADO
    NOMBRE:    IÑIGO


*/



/*


             CUATRO POSIBLES ALGORITMOS PARA EL PROBLEMA DE LA RAÍZ CUADRADA ENTERA


    1) Especifica y verifica en Dafny los siguientes cuatro algoritmos para resolver 
       el problema de la raíz cuadrada entera de un número natural.

    2) Compara la eficiencia de los cuatro algoritmos en C++ midiendo sus tiempos de 
       ejecución como hiciste en la Práctica 1. 

    3) Compara la eficiencia de los cuatro algoritmos obteniendo en Python las gráficas 
       de los tiempos de complejidad como hiciste en la Práctica 1. Visualiza las 
       funciones que determinan el orden de complejidad de cada uno de los algoritmos.


*/



/*


	ALGORITMO 1:

 
	{ P : n >= 0 }

	  fun raiz_ent1 (n : ent) dev r : ent { O(√n) }

	     r := 0 ;

             { I : r >= 0 /\ r^2 <= n }
             { C : n - r^2 }

             mientras n >= (r + 1) * (r + 1) hacer

			r := r + 1 ;

             fmientras
        
          ffun

        { Q : r^2 <= n < (r + 1)^2 }


*/
#nueva
requires n >= 0
ensures r * r <= n < (r + 1) * (r + 1)
{
   r := 0 ;
   while n >= (r + 1) * (r + 1)
            invariant r >= 0 && r * r = n
            decreases n - r * r
            ...
}

method raiz_ent1 (n : int) returns (r : int)
   requires n >= 0
   ensures r * r <= n < (r + 1) * (r + 1)
{
   r := 0 ;
   while n >= (r + 1) * (r + 1)
      invariant r >= 0 && r * r = n
      decreases n - r * r
   {
      r := r + 1
   }
}



/*


	ALGORITMO 2:

 
	{ P : n >= 0 }

	  fun raiz_ent2 (n : ent) dev r : ent { O(n) }

	     r := n ;

             { I : r >= 0 /\ n >= 0 /\ n < (r + 1)^2  }
             { C : r }

             mientras r * r > n hacer

			r := r - 1 ;

             fmientras
        
          ffun

        { Q : r^2 <= n < (r + 1)^2 }


*/





/*

     
     ALGORITMO 3:


     { P : n >= 0 }

       fun raiz_ent3 (n : ent) dev r : ent { O(log(n)) }

           var y, h : ent ;

           < r, y > := < 0, n + 1 > ;

           { I : r^2 <= n < y^2 /\ r < y <= n + 1 }
           { C : y - r }

           mientras y /= r + 1 hacer

		h := (r + y) div 2 ;

		if h * h <= n entonces r := h ;
                sino y := h ;
                fsi

	   fmientras
 
       ffun

     { Q : r^2 <= n < (r + 1)^2 }


*/





/*

	ALGORITMO 4: 


	{ P : a^2 <= n /\ n < b^2 /\ b >= a + 1 }

          fun raiz_ent4(n : ent, a : ent, b : ent) dev r : ent { O(log(n)) }

              var m : ent ;

              casos 

                 b = a + 1 ----> r := a  ;

              [] b > a + 1 ----> m := (a + b) div 2 ;

                                 casos 

                                    m * m <= n ----> r := raiz_ent4(n, m, b)

                                 [] m * m >  n ----> r := raiz_ent4(n, a, m)

                                 fcasos

              fcasos

          ffun 

	{ Q : r^2 <= n < (r + 1)^2 }


*/





/* 

     Programa principal para probar los algoritmos

*/



method Main()
{

   var r : int ;

   r := raiz_ent1(17) ;
   print(r) ;

   print("\n") ;

   r := raiz_ent2(17) ;
   print(r) ;

   print("\n") ;

   r := raiz_ent3(17) ;
   print(r) ;

   print("\n") ;

   r := raiz_ent4(17, 0, 17) ;
   print(r) ;

}