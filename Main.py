from Functions import Functions
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
from scipy.optimize import differential_evolution

def main():
    
    func = Functions()
    
    functions = ['Rastrigin', 'Ackley','Rosenbrock', 'Beale','Goldstein_Price',
                 'Booth','Bukin','Matyas','Sphere','Himmelblau']
    
    strategies = ['best1bin','best1exp','randtobest1exp','best2bin','best2exp']
    
    bounds = []

 
    st.title('Algorytmy ewolucyjne')
    st.subheader('Projekt 2: Ewolucja różnicowa')
    
    st.sidebar.subheader('Wybierz funkcję do optymalizacji:')
    _func = st.sidebar.radio(
        ' ',
        functions
    )
    
    parameters = pd.DataFrame({
        'Parametr':['x','fun, jac, hess','nfev, njev, nhev','nit','message','success',], 
        'Opis':['Rozwiązanie optymalizacji','Wartości funkcji celu, jej jakobian i hesjan (jeśli są dostępne)','Liczba ocen funkcji celu oraz jej jakobianu i hesjanu','Liczba iteracji','Informacja zwrotna','Czy optymalizator zakończył pracę z powodzeniem']
    })
    
    st.sidebar.table(parameters)
    st.markdown('---')
    
    leftCol, rightCol = st.columns(2)
    
    with leftCol:
        startButton = st.button('Optymalizacja')
        if startButton:
            
            if _func == functions[0]:
                bounds = [(-5.12, 5.12), (-5.12, 5.12)]
                for strategy in strategies:
                    result = differential_evolution(func.Rastrigin, bounds, strategy=strategy,disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[1]:
                bounds = [(-5,5), (-5,5)]
                for strategy in strategies:
                    result = differential_evolution(func.Ackley, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                
            if _func == functions[2]:
                bounds = [(-2,10), (-2,10)]
                for strategy in strategies:
                    result = differential_evolution(func.Rosenbrock, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[3]:
                bounds = [(-4.5,4.5), (-4.5,4.5)]
                for strategy in strategies:
                    result = differential_evolution(func.Beale, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[4]:
                bounds = [(-2,2), (-2,2)]
                for strategy in strategies:
                    result = differential_evolution(func.Goldstein_Price, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[5]:
                bounds = [(-10,10), (-10,10)]
                for strategy in strategies:
                    result = differential_evolution(func.Booth, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
                    
            if _func == functions[6]:
                bounds = [(-15,-5), (-3,3)]
                for strategy in strategies:
                    result = differential_evolution(func.Bukin, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[7]:
                bounds = [(-10,10), (-10,10)]
                for strategy in strategies:
                    result = differential_evolution(func.Matyas, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[8]:
                bounds = [(-3,3), (-3,3)]
                for strategy in strategies:
                    result = differential_evolution(func.Sphere, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                    
            if _func == functions[9]:
                bounds = [(-5,5), (-5,5)]
                for strategy in strategies:
                    result = differential_evolution(func.Himmelblau, bounds, strategy=strategy, disp=True, polish=True, updating='immediate', popsize=250)
                    st.write('Wyniki dla schematu mutacji: ', strategy)
                    st.table(result)
                    st.markdown('---')
                
    with rightCol:
        if (bounds != []):
            x = np.linspace(bounds[0][0],bounds[0][1],500)
            y = np.linspace(bounds[1][0],bounds[1][1],500)
            X,Y = np.meshgrid(x,y)

            if _func == functions[0]:
                Z = func.Rastrigin([X,Y])
                
            if _func == functions[1]:
                Z = func.Ackley([X,Y])
                
            if _func == functions[2]:
                Z = func.Rosenbrock([X,Y])
                
            if _func == functions[3]:
                Z = func.Beale([X,Y])
                
            if _func == functions[4]:
                Z = func.Goldstein_Price([X,Y])
                
            if _func == functions[5]:
                Z = func.Booth([X,Y])
                
            if _func == functions[6]:
                Z = func.Bukin([X,Y])
                
            if _func == functions[7]:
                Z = func.Matyas([X,Y])
                
            if _func == functions[8]:
                Z = func.Sphere([X,Y])
                
            if _func == functions[9]:
                Z = func.Himmelblau([X,Y])
                
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z,cmap='viridis', edgecolor='none')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            st.pyplot(fig)

main()