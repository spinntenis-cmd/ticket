object DBticket: TDBticket
  Height = 750
  Width = 1000
  PixelsPerInch = 120
  object conexao: TFDConnection
    Params.Strings = (
      'Database=ticket'
      'User_Name=root'
      'DriverID=MySQL')
    Connected = True
    LoginPrompt = False
    Left = 104
    Top = 128
  end
  object FDTicket: TFDTable
    IndexFieldNames = 'id'
    Connection = conexao
    ResourceOptions.AssignedValues = [rvEscapeExpand]
    TableName = 'ticket.cadastros'
    Left = 232
    Top = 128
    object FDTicketid: TFDAutoIncField
      FieldName = 'id'
      Origin = 'id'
      ProviderFlags = [pfInWhere, pfInKey]
      ReadOnly = False
    end
    object FDTicketFuncionarios: TStringField
      FieldName = 'Funcionarios'
      Origin = 'Funcionarios'
      Required = True
      Size = 50
    end
    object FDTicketTickets: TStringField
      FieldName = 'Tickets'
      Origin = 'Tickets'
      Required = True
      Size = 50
    end
    object FDTicketRelatorios: TDateField
      FieldName = 'Relatorios'
      Origin = 'Relatorios'
      Required = True
    end
  end
  object DTticket: TDataSource
    DataSet = FDTicket
    Left = 360
    Top = 128
  end
end
