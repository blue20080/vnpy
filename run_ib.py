from vnpy_chartwizard import ChartWizardApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_datamanager import DataManagerApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_portfoliomanager import PortfolioManagerApp

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ib import IbGateway




def main():
    """主入口函数"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(IbGateway)
    main_engine.add_app(DataManagerApp)
    main_engine.add_app(ChartWizardApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(PortfolioManagerApp)
    main_engine.add_app(DataManagerApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()