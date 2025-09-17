unit UnitConexão;

interface

uses
  System.SysUtils, System.Classes, FireDAC.Stan.Intf, FireDAC.Stan.Option,
  FireDAC.Stan.Error, FireDAC.UI.Intf, FireDAC.Phys.Intf, FireDAC.Stan.Def,
  FireDAC.Stan.Pool, FireDAC.Stan.Async, FireDAC.Phys, FireDAC.Phys.MySQL,
  FireDAC.Phys.MySQLDef, FireDAC.VCLUI.Wait, FireDAC.Stan.Param, FireDAC.DatS,
  FireDAC.DApt.Intf, FireDAC.DApt, Data.DB, FireDAC.Comp.DataSet,
  FireDAC.Comp.Client;

type
  TDBticket = class(TDataModule)
    conexao: TFDConnection;
    FDTicket: TFDTable;
    DTticket: TDataSource;
    FDTicketid: TFDAutoIncField;
    FDTicketFuncionarios: TStringField;
    FDTicketTickets: TStringField;
    FDTicketRelatorios: TDateField;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  DBticket: TDBticket;

implementation

{%CLASSGROUP 'Vcl.Controls.TControl'}

{$R *.dfm}

end.
