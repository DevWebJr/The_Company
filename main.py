from Module.SimulationManager.Simulation import Simulation


if __name__ == '__main__':
    
    simulation = Simulation()
    duration = simulation.choose_duration()
    list_of_of_companies = simulation.load_data_company()
    simulation.start(list_of_of_companies, duration)
