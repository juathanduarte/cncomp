def MetSecante(funcao, x0, x1, precisao, n_iter):
  k = 0
  x_barra = None
  
  f_x0 = funcao(x0)
  f_x1 = funcao(x1)

  if (abs(f_x0) < precisao):
    x_barra = x0
  elif (abs(f_x1) < precisao or abs(x1 - x0) < precisao):
    x_barra = x1

  while ( (abs(f_x0) >= precisao or abs(f_x1) >= precisao) and k < n_iter):
    x2 = x1 - (f_x1 / (f_x1 - f_x0)) * (x1 - x0)
    if (abs(funcao(x2)) < precisao or abs(x2 - x1) < precisao):
      x_barra = x2
    x0 = x1
    x1 = x2
    f_x0 = funcao(x0)
    f_x1 = funcao(x1)
    k = k + 1

  print("RAIZ APROXIMADA =", x_barra, "\tk =", k, "(Secante)\n")