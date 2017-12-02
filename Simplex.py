from pymprog import * 

xid, rid = range(3), range(3)
c = (10.0, 6.0, 4.0)        #funçao objetivo Max

mat = [ (1.0, 1.0, 1.0),    # 1 restrião 
        (10.0, 4.0, 5.0),   # 2 restricao
        (2.0, 2.0, 6.0)]    # 3 restrição

b = (100.0, 
     600.0, 
     300.0)   #termos independetes

#Definicao do problema

begin('basic')   #Defindo como basico

verbose(True)

x = var(xid, 'X') #Criar variaveis
print('\n')

maximize(sum(c[i]*x[i] for i in xid), 'Função Objetivo:')

#Conjunto de Restriçoes

r = st(sum(x[j]*mat[i][j] for j in xid) <= b[i] for i in rid)

solve() #Solucao e Informe

print ("Solucao:", status())  #verifica se a solucao é otima
print ('\nZ = %g;' % vobj())  # Valor Max função Objetivo

#IMPRIMIR valores variaveis e primarias e finais
print (';\n'.join('%s = %g {FINAL: %g}' % (
   x[i].name, x[i].primal, x[i].dual)
                    for i in xid))

print (';\n'.join('  %s = %g {FINAL: %g}' % (
   r[i].name, r[i].primal, r[i].dual)
                    for i in rid))
 
#print (reportKKT())
#print ("Environment:", env)
#for pn in dir(env):
#    if pn[:2]=='__'==pn[-2:]: continue
#    print (pn, getattr(env, pn))
# 
#print (' ')
#print (evaluate(sum(x[i]*(i+x[i])**2 for i in xid)))
#
#print (sum(x[i].primal*(i+x[i].primal)**2 for i in xid))

end() #Finalizar Algortimo